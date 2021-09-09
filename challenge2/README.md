# nitish-challenge-code
This python script runs on azure virtual machine , gets it metadata, print it and also allows user to get value of any key in that metadata. 



- Function metadata() gets metdata of instance and print json response on terminal
- Function fetch(data,v) accepts two arguements:
    - data : json response from metadata() function
    - v : Key whose value is required by user

To run script:

`python metadata.py`

This will prmpt user to give any required key ( For e.g. Enter Key name: privateIpAddress)

**Output**
- privateIpAddress is -> 10.x.x.x
- computerName is -> nnxxxxvm1



*This code is tested with python 2.7.18.If using python3 then replace raw_input weith input*
