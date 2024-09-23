#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT11.h>

const char *ssid = "Uaifai";
const char *password = "Cida@vicente07";
const char *supabaseUrl = "https://vkrlyyyvattgjcwimumr.supabase.co";
const char *supabaseApiKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrcmx5eXl2YXR0Z2pjd2ltdW1yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE4NDU5MTEsImV4cCI6MjAzNzQyMTkxMX0.RQYD0a8Z3jBXCsuglOSgGMbhisZEgtOVSdHDeTabCIk";


DHT11 dht(26);
const int RelePin = 4;
const int sensorUmidade = 34;
const int limiarSeco = 50;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  pinMode(sensorUmidade, INPUT);
  pinMode(RelePin, OUTPUT);
  digitalWrite(RelePin, LOW);


  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");
}

void loop() {
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
    if (leitura < limiarSeco) {
      digitalWrite(RelePin, LOW);
    }else{
      digitalWrite(RelePin, HIGH);
  }


    delay(1000);
  
}
