
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT11.h>
#include <WebServer.h>  // Biblioteca do servidor web

const char *ssid = "Casa";
const char *password = "nildapereira";
const char *supabaseUrl = "https://vkrlyyyvattgjcwimumr.supabase.co";
const char *supabaseApiKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInZrcmx5eXl2YXR0Z2pjd2ltdW1yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE4NDU5MTEsImV4cCI6MjAzNzQyMTkxMX0.RQYD0a8Z3jBXCsuglOSgGMbhisZEgtOVSdHDeTabCIk";

DHT11 dht(26);
const int RelePin = 4;
const int sensorUmidade = 34;
const int limiarSeco = 50;
bool controleManual = false;

WebServer server(80);  // Instância do servidor na porta 80

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  pinMode(sensorUmidade, INPUT);
  pinMode(RelePin, OUTPUT);
  digitalWrite(RelePin, HIGH);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");
  Serial.print("IP do ESP32: ");
  Serial.println(WiFi.localIP());

  // Configurações do servidor HTTP
  server.on("/rele/on", ligarRele);                      // Rota para ligar o relé
  server.on("/rele/off", desligarRele);                  // Rota para desligar o relé
  server.on("/get_sensores", getSensores);               // Rota para obter os dados dos sensores
  server.on("/set_controle_manual", setControleManual);  // Rota para habilitar/desabilitar controle manual

  server.begin();  // Inicia o servidor
  Serial.println("Servidor HTTP iniciado");
}

void loop() {
  server.handleClient();  // Processa as requisições HTTP

  int temperatura = 0;
  int umidade = 0;
  int result = dht.readTemperatureHumidity(temperatura, umidade);
  int leitura = analogRead(sensorUmidade);
  leitura = map(leitura, 4095, 0, 0, 100);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String jsonPayload = "{";
    jsonPayload += "\"umidade_solo\":" + String(leitura) + ",";
    jsonPayload += "\"temperatura\":" + String(temperatura) + ",";
    jsonPayload += "\"umidade_ar\":" + String(umidade);
    jsonPayload += "}";

    String url = String(supabaseUrl) + "/rest/v1/sensor_data";
    http.begin(url);
    http.addHeader("Content-Type", "application/json");
    http.addHeader("apikey", supabaseApiKey);
    http.addHeader("Authorization", "Bearer " + String(supabaseApiKey));

    int httpCode = http.POST(jsonPayload);
    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(payload);
    } else {
      Serial.print("Erro na requisição: ");
      Serial.println(httpCode);
    }
    http.end();
  }

  // Controle automático do relé
  if (!controleManual) {  // Só controla automaticamente se o modo manual não estiver ativado
    if (leitura < limiarSeco) {
      digitalWrite(RelePin, LOW);  // Liga o relé
    } else {
      digitalWrite(RelePin, HIGH);  // Desliga o relé
    }
  }

  delay(1000);  // Intervalo de 1 segundo entre leituras
}

// Função para ligar o relé via HTTP
void ligarRele() {
  controleManual = true;       // Ativa o controle manual
  digitalWrite(RelePin, LOW);  // Liga o relé
  server.send(200, "text/plain", "Relé ligado");
  Serial.println("Relé ligado via HTTP");
}

// Função para desligar o relé via HTTP
void desligarRele() {
  controleManual = true;        // Ativa o controle manual
  digitalWrite(RelePin, HIGH);  // Desliga o relé
  server.send(200, "text/plain", "Relé desligado");
  Serial.println("Relé desligado via HTTP");
}

// Função para retornar dados dos sensores via HTTP
void getSensores() {
  int temperatura = 0;
  int umidade = 0;
  int result = dht.readTemperatureHumidity(temperatura, umidade);
  int leitura = analogRead(sensorUmidade);
  leitura = map(leitura, 4095, 0, 0, 100);

  String jsonResponse = "{";
  jsonResponse += "\"temperatura\":" + String(temperatura) + ",";
  jsonResponse += "\"umidade_ar\":" + String(umidade) + ",";
  jsonResponse += "\"umidade_solo\":" + String(leitura);
  jsonResponse += "}";

  server.send(200, "application/json", jsonResponse);
  Serial.println("Dados dos sensores enviados via HTTP");
}

// Função para ativar ou desativar o controle manual via HTTP
void setControleManual() {
  if (server.hasArg("manual")) {
    String modo = server.arg("manual");
    if (modo == "on") {
      controleManual = true;
      server.send(200, "text/plain", "Controle manual ativado");
      Serial.println("Controle manual ativado");
    } else if (modo == "off") {
      controleManual = false;
      server.send(200, "text/plain", "Controle manual desativado");
      Serial.println("Controle manual desativado");
    } else {
      server.send(400, "text/plain", "Argumento inválido");
    }
  } else {
    server.send(400, "text/plain", "Parâmetro manual não fornecido");
  }
}
