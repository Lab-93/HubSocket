# Lab-93 Socket Server API Hub
The `SocketServer()` class object defines a kind of http echo server designed to re-
broadcast information sent to it in the form of a JSON object.  Information sent to this
hub socket is continuously sent until the hub recieves a new packet of information.

This system utilizes the concept of `request headers` to assign destinations to the
appropriate recipient in a `UDP` like manner.  For example; a downstream client listening
out for financial analysis would have their daemon constantly joining the sockets
`response['financial analysis']` sub-header to their own `financial_report` object.

Services contributing to the state of the machine do so by writing a nested dictionary
encoded as ASCII bytes to the SocketServer instance of their choosing.

## Usage Example
```
python3 -m HubSocket --host 0.0.0.0 --port 65535
```
