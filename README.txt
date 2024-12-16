README FILE 

4<=>CLIENT-SERVER (basic folder): 

 We have two python files named “client.py” and “server.py” in basic folder.  

Execution steps: 

Two run these files:  

1. Open terminal, go to “/home/p4/tutorials/exercises/basic” 

2. Run “make clean” 

3. Run “make run” 

4. You are now on the mininet prompt. 

5. Run below commands to open the Host terminals: 

     a. “xterm h1” 

     b. “xterm h2” 

6. Commands to run on h2’s terminal 

     a. bash h2-arp.sh (run once every time you run “make” above) 

     b. python server.py  

7. Command to run on h1’s terminal 

     a. bash h1-arp.sh (run once every time you run “make” above) 

     b. python client.py  

Then in h1’s terminal we must give input for “request method” which can be  

    I)” GET” 

	Then we give input for {key} we want. 

   II)” PUT” 

	Then we give input for {key} and {value} we want to insert. 

  III)” DELETE” 

	Then we give input for {key} we want to delete. 

  IV)” End” 

	The client-server connection closes. 

  V) any other string as request method => treated as bad request 

If there is any socket error at client or server side or any keyboard interrupt error => client –server connection closes. 

After sending requests we want we close client server connection by giving “End “as input for request method. 

We run "ctrl+c” to close server socket in h2 terminal. 

 

4<=>CLIENT-CACHE-SERVER (star folder): 

 We have two python files named “client.py” and “server.py” in basic folder.  

Execution steps: 

Command to run: 

1. Open terminal, go to “/home/p4/tutorials/exercises/basic” 

2. Run “make clean” 

3. Run “make run” 

4. You are now on the mininet prompt. 

5. Run below commands to open the Host terminals: 

     a. “xterm h1” 

     b. “xterm h2” 

     c. “xterm h3” 

6. Commands to run on h3’s terminal 

     a. bash h3-arp.sh (run once every time you run “make” above) 

     b. python server.py  

7. Command to run on h2’s terminal 

     a. bash h2-arp.sh (run once every time you run “make” above) 

     b. python cache.py 

8. Command to run on h1’s terminal 

     a. bash h1-arp.sh (run once every time you run “make” above) 

     b. python client.py 

Then in h1’s terminal we must give input for “request method” which can be  

    I)” GET” 

	Then we give input for {key} we want. 

   II)” PUT” 

	Then we give input for {key} and {value} we want to insert. 

  III)” DELETE” 

	Then we give input for {key} we want to delete. 

  IV)” End” 

	The client-server connection closes. 

  V) any other string as request method => treated as bad request 

If there is any socket error at client or server side or any keyboard interrupt error => client –server connection closes. 

After sending requests we want we close client server connection by giving “End “as input for request method. 

We run “ctrl+c” to close server socket in h3 terminal and to close cache socket in h2 terminal. 



=> All the pcap file are present in temp folder in there respective folder which are basic and star folders.
pcap file directories:
i)/CS21BTECH11063_Assignment2/basic/temp
ii)/CS21BTECH11063_Assignmnet2/star/temp

report files directories:
i)/CS21BTECH11063_Assignment2/basic/report/report.pdf
ii)/CS21BTECH11063_Assignmnet2/star/report/report.pdf

Question 6 answer is in respective reports.

