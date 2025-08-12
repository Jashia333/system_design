PUT commands :
 curl.exe -X PUT "http://localhost:9000/cache" `   
-H "Content-Type: application/json" `
-d "@data.json"

GET commands
curl.exe -X GET "http://localhost:9000/cache/size"
curl.exe -X GET "http://localhost:9000/cache/show"
