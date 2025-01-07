## kafka utility scripts

checkilg all topics:

docker exec -it {kafka-broker} kafka-topics --list --bootstrap-server localhost:9092

srating producer 

kafka-console-producer -\-broker-list localhost:9092 --topic transactions

running producer:
python src\producer.py
