# from here:

Note you have to install awscli and configure credentials.

https://docs.aws.amazon.com/lambda/latest/dg/python-image.html

create the s3 bucket.  Must be the same user whose keys match - that is me: Marilyn, not the root user.  Modify permissions and add  s3 role in when creating the lambda function LambdaS3FullAccess

docker build -t tests3 .
docker run -p 9000:8080  tests3:latest

docker run -p 9000:8080 -e AWS_ACCESS_KEY_ID="  " -e  AWS_SECRET_ACCESS_KEY="xxx" -e AWS_REGION="us-west-2" tests3:latest 

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin xxxxxx.dkr.ecr.us-west-2.amazonaws.com 


 aws ecr create-repository \
    --repository-name tests3 \
    --image-scanning-configuration scanOnPush=true \
    --region us-west-2


docker tag  tests3:latest xxxxxxxx.dkr.ecr.us-west-2.amazonaws.com/tests3:latest
docker push xxxxxx.dkr.ecr.us-west-2.amazonaws.com/tests3:latest            




https://dev.to/aws-builders/container-images-for-aws-lambda-with-python-286c
       

