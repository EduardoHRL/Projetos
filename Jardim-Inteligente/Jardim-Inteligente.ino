#include <HTTPClient.h>
#include <WebServer.h>
#include <WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

const char *ssid = "Casa";
const char *password = "nildapereira";
const char *supabaseUrl = "https://vkrlyyyvattgjcwimumr.supabase.co";
const char *supabaseApiKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrcmx5eXl2YXR0Z2pjd2ltdW1yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE4NDU5MTEsImV4cCI6MjAzNzQyMTkxMX0.RQYD0a8Z3jBXCsuglOSgGMbhisZEgtOVSdHDeTabCIk";

const int RelePin = 4;
const int sensorUmidade = 34;
const int limiarSeco = 50;
bool controleManual = false;

WebServer server(80);

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", -3 * 3600);

unsigned long ultimoEnvio = 0;
const unsigned long intervaloEnvio = 100000;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  pinMode(sensorUmidade, INPUT);
  pinMode(RelePin, OUTPUT);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }

  timeClient.begin();

  Serial.println("Conectado ao WiFi");
  Serial.print("IP do ESP32: ");
  Serial.println(WiFi.localIP());

  server.on("/rele/on", ligarRele);
  server.on("/rele/off", desligarRele);
  server.on("/get_sensores", getSensores);
  server.on("/set_controle_manual", setControleManual);

  server.begin();
  Serial.println("Servidor HTTP iniciado");
}

void loop() {
  server.handleClient();
  timeClient.update();

  unsigned long tempoAtual = millis();

  if (tempoAtual - ultimoEnvio >= intervaloEnvio) {
    ultimoEnvio = tempoAtual;

    time_t rawtime = timeClient.getEpochTime();
    struct tm *timeinfo = gmtime(&rawtime);
    char buffer[25];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%SZ", timeinfo);

    String Data = String(buffer);

    int leitura = analogRead(sensorUmidade);
    leitura = map(leitura, 4095, 0, 0, 100);

    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      String jsonPayload = "{";
      jsonPayload += "\"umidade_solo\":" + String(leitura) + ",";
      jsonPayload += "\"horario\":\"" + Data + "\"";
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
  }

  if (!controleManual) {
    int leitura = analogRead(sensorUmidade);
    leitura = map(leitura, 4095, 0, 0, 100);

    if (leitura < limiarSeco) {
      digitalWrite(RelePin, HIGH);  // Liga o relé
    } else {
      digitalWrite(RelePin, LOW);  // Desliga o relé
    }
  }
}

void ligarRele() {
  controleManual = true;
  digitalWrite(RelePin, HIGH);
  server.send(200, "text/plain", "Relé ligado");
  Serial.println("Relé ligado via HTTP");
}

void desligarRele() {
  controleManual = true;
  digitalWrite(RelePin, LOW);
  server.send(200, "text/plain", "Relé desligado");
  Serial.println("Relé desligado via HTTP");
}

void getSensores() {
  int leitura = analogRead(sensorUmidade);
  leitura = map(leitura, 4095, 0, 0, 100);

  String jsonResponse = "{";
  jsonResponse += "\"umidade_solo\":" + String(leitura);
  jsonResponse += "}";

  server.send(200, "application/json", jsonResponse);
  Serial.println("Dados dos sensores enviados via HTTP");
}

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
