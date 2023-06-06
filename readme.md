# api.submodules.hub
The `apiHub()` class object defines a tcp echo server for distributing a wide range of data from various back-end
sources to any number of front-end clients by providing a singular state-machine for storing information segmentally
as it is recieved.

Services contributing to the state of the machine do so by writing a nested dictionary as JSON bytes to the server
stream.
