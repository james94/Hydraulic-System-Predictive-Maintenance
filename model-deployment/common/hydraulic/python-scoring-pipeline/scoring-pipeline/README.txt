# Copyright 2018-2019 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

-------------------------------------------------------------------------------

                H2O DRIVERLESS AI STANDALONE PYTHON SCORING PIPELINE


                           PROPRIETARY LICENSE -

                USE OF THIS SCORING PIPELINE REQUIRES A VALID,
                ONGOING LICENSE AGREEMENT WITH H2O.AI.

                Please contact sales@h2o.ai for more information.

-------------------------------------------------------------------------------

This package contains an exported model and Python 3.6 source code examples
for productionizing models built using H2O Driverless AI.

The files in this package allow you to transform and score on new data in 
a couple of different ways:

    * From Python 3.6, you can import a scoring module, and then use the module 
      to transform and score on new data.
    * From other languages and platforms, you can use the TCP/HTTP scoring 
      service bundled with this package to call into the scoring pipeline module
      through remote procedure calls (RPC).

Requirements:

- The scoring module and scoring service are supported only on Linux with
  Python 3.6 and OpenBLAS. For installation instructions, see Appendix A.
- The scoring module and scoring service download additional packages at 
  install-time, and requires internet access. Depending on your network environment,
  you might need to set up internet access via a proxy.
- Valid Driverless AI license. Driverless AI requires a license to be specified in 
  order to run the Python Scoring Pipeline.
- ocl-icd-libopencl1 package

  - For RHEL/CentOS: Retrieve the EPEL 7 repo, and the run `yum install opencl-headers`
  - For Ubuntu: Run `apt install ocl-icd-libopencl1`


-------------------------------------------------------------------------------
DIRECTORY LISTING:

    example.py              An example Python script demonstrating how to 
                            import and score new records.

    run_example.sh          Runs example.py (also sets up a virtualenv with 
                            prerequisite libraries).

    tcp_server.py           A standalone TCP server for hosting scoring services.

    http_server.py          A standalone HTTP server for hosting scoring services.

    run_tcp_server.sh       Runs TCP scoring service (runs tcp_server.py).

    run_http_server.sh      Runs HTTP scoring service (runs http_server.py).

    example_client.py       An example Python script demonstrating how to 
                            communicate with the scoring server.

    run_tcp_client.sh       Demonstrates how to communicate with the scoring 
                            service via TCP (runs example_client.py).

    run_http_client.sh      Demonstrates how to communicate with the scoring 
                            service via HTTP (using curl).


-------------------------------------------------------------------------------
QUICKSTART - RECOMMENDED:

1. Download the TAR SH version of Driverless AI from https://www.h2o.ai/download/ 
   (for either Linux or IBM Power).
2. Use bash to execute the download. This creates a new dai-nnn folder.
3. Change directories into the new Driverless AI folder.
4. Run the following to install the Python Scoring Pipeline for your completed 
   Driverless AI experiment:

   ./dai-env.sh pip install /path/to/your/scoring_experiment.whl

5. Run the following command to run the included scoring pipeline example:

   DRIVERLESS_AI_LICENSE_KEY="pastekeyhere" SCORING_PIPELINE_INSTALL_DEPENDENCIES=0 ./dai-env.sh /path/to/your/run_example.sh


QUICKSTART - ALTERNATIVE:

If you intend to score from a Python program, run the scoring module example.
(Requires Linux and Python 3.6. See Appendix A.)

      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ bash run_example.sh


If you intend to score using a web service, run the HTTP scoring server example. 
(Requires Linux and Python 3.6. See Appendix A.)

      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ bash run_http_server.sh 
      $ bash run_http_client.sh


If you intend to score using a Thrift service,  run the TCP scoring server example.
(Requires Linux, Python 3.6 and Thrift. See Appendix A, B.)

      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ bash run_tcp_server.sh 
      $ bash run_tcp_client.sh


Notes:
- By default, the run_*.sh scripts mentioned above create a virtual environment
  using virtualenv and pip within which the python code is executed. They 
  can also leverage conda (Anaconda/Mininconda) to create conda virtual environment
  and install required package dependencies. The package manager to use is provided
  as an argument to the script. 

      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ bash run_example.sh --pm conda        (to use conda package manager)

      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ bash run_example.sh --pm pip          (to use pip package manager)
  
- If you experience errors while running any of the above scripts, please
  check to make sure your system has a properly installed and configured Python 3.6
  installation. To isolate and debug such problems, Appendix C describes how
  to set up and test the scoring module using a cleanroom Ubuntu 16.04 virtual
  machine.


-------------------------------------------------------------------------------
SCORING MODULE:

The scoring module is a Python module bundled into a standalone wheel file 
(name scoring_*.whl). All the prerequisites for the scoring module to work 
correctly are listed in the 'requirements.txt' file. To use the scoring module, 
all you have to do is create a Python virtualenv, install the prerequisites, 
and then import and use the scoring module as follows:

      ----- See 'example.py' for complete example. -----
      from scoring_487931_20170921174120_b4066 import Scorer
      scorer = Scorer()       # Create instance.
      score = scorer.score([  # Call score()
          7.416,              # sepal_len
          3.562,              # sepal_wid
          1.049,              # petal_len
          2.388,              # petal_wid
      ])


The scorer instance provides the following methods (and more):

      score(list)             Score one row (list of values).

      score_batch(df)         Score a Pandas dataframe.

      fit_transform_batch(df) Transform a Pandas dataframe.

      get_target_labels()     Get target column labels 
                              (for classification problems)


The process of importing and using the scoring module is demonstrated by the 
bash script 'run_example.sh', which effectively performs the following steps:

      ----- See 'run_example.sh' for complete example. -----
      $ virtualenv -p python3.6 env
      $ source env/bin/activate
      $ pip install -r requirements.txt
      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ python example.py
    


-------------------------------------------------------------------------------
SCORING SERVICE OVERVIEW:

The scoring service hosts the scoring module as a HTTP or TCP service. Doing 
this exposes all the functions of the scoring module through remote procedure
calls (RPC). 

In effect, this mechanism allows you to invoke scoring functions from languages
other than Python on the same computer, or from another computer on a shared 
network or the internet.

The scoring service can be started in two ways:

    * In TCP mode, the scoring service provides high-performance RPC calls via 
      Apache Thrift (https://thrift.apache.org/) using a binary wire protocol.

    * In HTTP mode, the scoring service provides JSON-RPC 2.0 calls served by 
      Tornado (http://www.tornadoweb.org).

Scoring operations can be performed on individual rows (row-by-row) or in batch 
mode (multiple rows at a time).



-------------------------------------------------------------------------------
SCORING SERVICE - TCP MODE (THRIFT):

The TCP mode allows you to use the scoring service from any language supported 
by Thrift, including C, C++, C#, Cocoa, D, Dart, Delphi, Go, Haxe, Java, 
Node.js, Lua, perl, PHP, Python, Ruby and Smalltalk. 

To start the scoring service in TCP mode, you will need to generate the Thrift 
bindings once, then run the server:

      ----- See 'run_tcp_server.sh' for complete example. -----
      $ thrift --gen py scoring.thrift
      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ python tcp_server.py --port=9090

See Appendix B for installing the Apache Thrift compiler.  Note that the Thrift 
compiler is only required at build-time. It is not a run time dependency,
i.e. once the scoring services are built and tested, you do not need to repeat 
this installation process on the machines where the scoring services are 
intended to be deployed.

To call the scoring service, simply generate the Thrift bindings for your 
language of choice, then make RPC calls via TCP sockets using Thrift's 
buffered transport in conjunction with its binary protocol. 

  
      ----- See 'run_tcp_client.sh' for complete example. -----
      $ thrift --gen py scoring.thrift


      ----- See 'example_client.py' for complete example. -----
      socket = TSocket.TSocket('localhost', 9090)
      transport = TTransport.TBufferedTransport(socket)
      protocol = TBinaryProtocol.TBinaryProtocol(transport)
      client = ScoringService.Client(protocol)
      transport.open()
      row = Row()
      row.sepalLen = 7.416  # sepal_len
      row.sepalWid = 3.562  # sepal_wid
      row.petalLen = 1.049  # petal_len
      row.petalWid = 2.388  # petal_wid
      scores = client.score(row)
      transport.close()


You can reproduce the exact same result from other languages, e.g. Java:

      $ thrift --gen java scoring.thrift

      // Dependencies: 
      // commons-codec-1.9.jar
      // commons-logging-1.2.jar
      // httpclient-4.4.1.jar
      // httpcore-4.4.1.jar
      // libthrift-0.10.0.jar
      // slf4j-api-1.7.12.jar

      import ai.h2o.scoring.Row;
      import ai.h2o.scoring.ScoringService;
      import org.apache.thrift.TException;
      import org.apache.thrift.protocol.TBinaryProtocol;
      import org.apache.thrift.transport.TSocket;
      import org.apache.thrift.transport.TTransport;
      import java.util.List;

      public class Main {
        public static void main(String[] args) {
          try {
            TTransport transport = new TSocket("localhost", 9090);
            transport.open();

            ScoringService.Client client = new ScoringService.Client(
              new TBinaryProtocol(transport));

            Row row = new Row(7.642, 3.436, 6.721, 1.020);
            List<Double> scores = client.score(row);
            System.out.println(scores);

            transport.close();
          } catch (TException ex) {
            ex.printStackTrace();
          }
        }
      }


-------------------------------------------------------------------------------
SCORING SERVICE - HTTP MODE (JSON-RPC 2.0)

The HTTP mode allows you to use the scoring service using plaintext JSON-RPC 
calls. This is usually less performant compared to Thrift, but has the advantage 
of being usable from any HTTP client library in your language of choice,
without any dependency on Thrift. 

For JSON-RPC documentation, see http://www.jsonrpc.org/specification .

To start the scoring service in HTTP mode:

      ----- See 'run_http_server.sh' for complete example. -----
      $ export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
      $ python http_server.py --port=9090


To invoke scoring methods, compose a JSON-RPC message and make a HTTP POST 
request to http://host:port/rpc as follows:

      ----- See 'run_http_client.sh' for complete example. -----
      $ curl http://localhost:9090/rpc \
        --header "Content-Type: application/json" \
        --data @- <<EOF
       {
        "id": 1,
        "method": "score",
        "params": {
          "row": [ 7.486, 3.277, 4.755, 2.354 ]
        }
       }
      EOF


Similarly, you can use any HTTP client library to reproduce the above result. 
For example, from Python, you can use the requests module as follows:

      import requests
      row = [7.486, 3.277, 4.755, 2.354]
      req = dict(id=1, method='score', params=dict(row=row))
      res = requests.post('http://localhost:9090/rpc', data=req)
      print(res.json()['result'])


-------------------------------------------------------------------------------
APPENDIX A. INSTALLING PYTHON 3.6 and OpenBLAS:

Installing Python3.6 on Ubuntu 16.10+:

      $ sudo apt install python3.6 python3.6-dev python3-pip python3-dev \
          python-virtualenv python3-virtualenv libopenblas-dev


Installing Python3.6 on Ubuntu 16.04:

      $ sudo add-apt-repository ppa:deadsnakes/ppa
      $ sudo apt-get update
      $ sudo apt-get install python3.6 python3.6-dev python3-pip python3-dev \
          python-virtualenv python3-virtualenv libopenblas-dev

Installing conda

You can install conda either using Anaconda or Miniconda. Follow instructions
in the links below

Anaconda - https://docs.anaconda.com/anaconda/install.html
Miniconda - https://conda.io/docs/user-guide/install/index.html

-------------------------------------------------------------------------------
APPENDIX B. INSTALLING THE APACHE THRIFT COMPILER:

Also refer to Thrift documentation at  
https://thrift.apache.org/docs/BuildingFromSource.

      $ sudo apt-get install automake bison flex g++ git libevent-dev \
          libssl-dev libtool make pkg-config libboost-all-dev ant
      $ wget https://github.com/apache/thrift/archive/0.10.0.tar.gz
      $ tar -xvf 0.10.0.tar.gz
      $ cd thrift-0.10.0
      $ ./bootstrap.sh
      $ ./configure
      $ make
      $ sudo make install

To refresh the runtime shared after installing Thrift
      $ sudo ldconfig /usr/local/lib

-------------------------------------------------------------------------------

APPENDIX C. LICENSE SPECIFICATION

Driverless AI requires a license to be specified in order to run the Python Scoring Pipeline. 
The license can be specified via an environment variable:

 - DRIVERLESS_AI_LICENSE_FILE: Path to the Driverless AI license file, or
 - DRIVERLESS_AI_LICENSE_KEY: The Driverless AI license key (Base64 encoded string)

    # Set DRIVERLESS_AI_LICENSE_FILE, the path to the Driverless AI license file
    %env DRIVERLESS_AI_LICENSE_FILE="/home/ubuntu/license/license.sig"


    # Set DRIVERLESS_AI_LICENSE_KEY, the Driverless AI license key (Base64 encoded string)
    %env DRIVERLESS_AI_LICENSE_KEY="oLqLZXMI0y..."


-------------------------------------------------------------------------------
APPENDIX D. TROUBLESHOOTING PYTHON ENVIRONMENT ISSUES:

The following instructions describe how to set up a cleanroom Ubuntu 16.04
  virtual machine to test that this scoring pipeline works correctly.

Prerequisites:

- Install Virtualbox: sudo apt-get install virtualbox
- Install Vagrant: https://www.vagrantup.com/downloads.html


STEP 1: Create configuration files for Vagrant

- bootstrap.sh: contains commands to set up Python 3.6 and OpenBLAS.
- Vagrantfile: contains virtual machine configuration instructions for Vagrant and VirtualBox.


----- bootstrap.sh -----

#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get -y install apt-utils build-essential python-software-properties software-properties-common zip libopenblas-dev
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update -yqq
sudo apt-get install -y python3.6 python3.6-dev python3-pip python3-dev python-virtualenv python3-virtualenv

# end of bootstrap.sh

----- Vagrantfile -----

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, path: "bootstrap.sh", privileged: false
  config.vm.hostname = "h2o"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
  end
end

# end of Vagrantfile

STEP 2: Launch the VM and SSH into it. 

Note that we're also placing the scoring pipeline in the same directory so that 
  we can access it later inside the VM.

cp /path/to/scorer.zip .
vagrant up
vagrant ssh



STEP 3: Test the scoring pipeline inside the virtual machine.

cp /vagrant/scorer.zip .
unzip scorer.zip 
cd scoring-pipeline/
export DRIVERLESS_AI_LICENSE_FILE="/path/to/license.sig"
bash run_example.sh


At this point you should see scores printed out on the terminal. If not, contact us at support@h2o.ai.
