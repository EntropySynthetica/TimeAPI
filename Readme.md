
# Time Rest API Server
A simple Rest server to provide the current time for IOT projects.  Inspired by worldtimeapi.org

### To Build
`docker build -t timeapi .`

### To Run
`docker run -d -p 30180:80 --name timeapi timeapi`

### To access
http://<server_ip>:<port>/time

Returns the UTC time

http://<server_ip>:<port>/time/<timezone_name>

Returns the time for the desired timezone.  Example:

http://<server_ip>:<port>/time/america/chicago

###
Prebuilt docker image at https://hub.docker.com/r/entropysynthetica/timeapi
