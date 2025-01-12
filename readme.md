## kafka utility scripts

checkilg all topics:

docker exec -it {kafka-broker} kafka-topics --list --bootstrap-server localhost:9092

srating producer

kafka-console-producer -\-broker-list localhost:9092 --topic transactions

running producer:
python src\producer.py

kafka-console-consumer --bootstrap-server  kafka:9092 --topic user-login --from-beginning

docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic Transcations --from-beginning


kafka-streaming-pipeline-python-produc
