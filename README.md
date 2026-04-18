# CubeColorService
A system where the cube's color is controlled by an external HTTP service

## How to run the service
Run python color_service.py to begin the https service. Open your browser and paste http://localhost:8080. While this program is running, you will be able to change the color by clicking on the current color, choosing a new color in the color picker, and confirming it. Make sure this is running before clicking play in unity!

## How Unity communicates with the service
Unity sends a get request to the service, and it responds with a JSON object containing the color. Unity reads this color and applies it to the cube. 

## How to change and test the cube's color
While the python program is running and you have the service open in the browser, press play in Unity. Change the color in the browser and the cube in Unity should change color as well. There is a tool to change the color in the inspector as well under Pick a Color. If you decide to change the color with the inspector, refresh the http service and the current color should update. 

## Things I would add if this were a production service
For security, I would definitely add an API key or implement data encryption since it is not an https service. I would also store colors in a database so the color doesn't reset to the hardcoded default color every time we re run the service, and utilize a logging system to keep track of when the color was changed and who changed it such as the built in module in python. Also, since I am using ThreadingMixIn, I create a new thread for every request, which can build up quickly if there are multiple people using the service. I would implement a thread pool to prevent memory overload in case this happens. 
