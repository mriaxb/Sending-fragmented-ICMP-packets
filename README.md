# Sending-fragmented-ICMP-packets


### Installation

_First of all, you have to make sure you have everything you need installed._

1. Install VS Code file at [https://code.visualstudio.com/download]
   Then follow the installation instructions bellow
   
     Linux:
      ```sh
       sudo apt install ./downloaded_file.deb
      ```
   
     Windows:
   
      After downloading the installer file, follow the installation instructions.
      You can use this site as a reference for installation [https://code.visualstudio.com/docs/setup/windows]


3. Install pyhton 

    Linux (Debian / Ubunto):
    ```sh
       sudo apt update
       sudo apt install python3
    ```
   
    Windows:
   
      Download the executable installer at [https://www.python.org/downloads/windows/] run the program and follow the installation steps 

### Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/mriaxb/Sending-fragmented-ICMP-packets.git
   ```
2. Change the file with your personalized information
   ```sh
    # destination IP and custom payload 
    target_ip = "0.0.0.0 <- your destination IP"
    custom_payload = "This is a payload to be fragmented <- your custom payload"
   ```
3. Run the program

    Linux:
     ```sh
        python3 icmp_packets.py
     ```
    Windows:
     ```sh
        python3 icmp_packets.py
     ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

