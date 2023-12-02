#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "ESP32";
const char* password = "12345678";

IPAddress local_ip(192,168,5,1);
IPAddress gateway(192,168,5,1);
IPAddress subnet(255,255,255,0);

void setup() 
{ Serial.begin(115200);
  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  delay(100);
 }

void loop() { 
}
