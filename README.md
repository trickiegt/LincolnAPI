# LincolnAPI

How I got my sessionID and Tokens

I installed mitmp (Man in the middle proxy)

Installed BlueStacks and then looked up how to Root BlueStacks
---Once rooted -> install Root Certificate Manager from google playstore

Installed ProxyCap
--Used to force any connections from BlueStacks to the proxy server (mitm)

Once all of those are installed and bluestacks is rooted, I ran the web version of mitm which brings up a webpage to monitor the traffic
Then I setup ProxyCap to point http connections to mitm proxy server & https connections to the same
Then I setup rules in ProxyCap to force connections from BlueStacks to use the previously mentioned proxies for http/https
----program name "HD-Player.exe" and port 80 for http && port 443 for HTTPS
Next - in bluestacks open a web browser and goto http://mitm.it -> download the certificate
Then open root certificate manager and import the downloaded cert file

Next I clear the current results in the mitm web interface
Then open the Lincoln Way app & review the traffic in the mitm web interface, you should be able to find the SessionID
-If not, clear the results again and then in the lincoln app, request door lock & check the web interface agian
