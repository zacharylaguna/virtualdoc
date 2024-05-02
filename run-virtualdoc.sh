#!/bin/bash
echo "hi" > /home/ubuntu/TESTING_THIS_VIRTUALDOC.txt

nodepath=$(which node); sudo ln -s $nodepath /usr/bin/node

# run client
cd /home/ubuntu/virtualdoc/nextjs-flask/
export PATH="$PATH:/home/ubuntu/.nvm/versions/node/v20.12.1/bin"
export PATH="$PATH:/home/ubuntu/.local/bin:/usr/bin/python3"
sudo apt install -y python3-pip > /home/ubuntu/OUTPUT-PIP.txt
npm run dev > /home/ubuntu/OUTPUT.txt
