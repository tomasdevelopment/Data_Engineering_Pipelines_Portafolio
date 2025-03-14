AWS Lambda Deployment with Docker (Ubuntu EC2 Instance)


FIle structure 
├── /content
│ ├── app.py
│ ├── bootstrap.py
│ └── requirements.txt
└── Dockerfile


Setup PEM File Permissions (Windows)

Restrict access only to your current user:

icacls "C:\Users\tomas\Downloads\pandas_json_project_aws.pem" /inheritance:r /grant %USERNAME%:F

Verify permissions:

icacls  "C:\Users\tomas\Downloads\pandas_json_project_aws.pem"

Connect to AWS Ubuntu Instance

ssh -i "C:\Users\tomas\Downloads\pandas_json_project_aws.pem" ubuntu@ec2-3-144-250-178.us-east-2.compute.amazonaws.com


Transfer Files to Ubuntu EC2

scp -i "C:\Users\tomas\Downloads\pandas_json_project_aws.pem" "C:\Users\tomas\Desktop\OCI.zip" ubuntu@ec2-3-144-250-178.us-east-2.compute.amazonaws.com:/home/ubuntu/

Prepare Ubuntu Environment

wget https://d6opu47qoi4ee.cloudfront.net/dockerinstallscript.sh
bash ./dockerinstallscript.sh
sudo apt install unzip awscli -y
unzip OCI.zip

Connect to AWS Ubuntu Instance

Configure AWS CLI

aws configure

Skip the access key and secret access key (press Enter).

Enter the region as us-east-1.

Enter format as json.

Docker Image Creation

Navigate to your Dockerfile directory (OCI) and run:

sudo docker build -t lambda_json_ecr .

sudo docker images


Push Docker Image to AWS ECR

Login to AWS ECR:

aws ecr get-login-password --region us-east-2 | sudo docker login --username AWS --password-stdin 863518419981.dkr.ecr.us-east-2.amazonaws.com

Build and tag Docker image:
sudo docker build -t lambda_json_pandas .
sudo docker tag lambda_json_pandas:latest 863518419981.dkr.ecr.us-east-2.amazonaws.com/pandas_json_project_repository:latest


sudo docker push 863518419981.dkr.ecr.us-east-2.amazonaws.com/pandas_json_project_repository:latest



Quick SSH Access Reference
ssh -i /path/to/your-key.pem ubuntu@3.144.250.179





