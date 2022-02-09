import apache_beam as beam
import apache_beam.transforms.window as window
from apache_beam.io.external.kafka import ReadFromKafka, WriteToKafka

brokers = 'localhost:9092'
kafka_topic = 'stocks'

def run_pipeline():
  with beam.Pipeline() as p:
    (p
     | 'Read from Kafka' >> ReadFromKafka(consumer_config=
                                {'bootstrap.servers': brokers}
#                                ,'auto.offset.reset': 'latest'},
                            , topics=[kafka_topic])
     | 'Print' >> beam.Map(print)
    )
    #  | 'Window of 10 seconds' >> beam.WindowInto(window.FixedWindows(10))
    #  | 'Group by key' >> beam.GroupByKey()
    #  | 'Sum word counts' >> beam.Map(lambda kv: (kv[0], sum(kv[1])))
    #  | 'Write to Kafka' >> WriteToKafka(producer_config={'bootstrap.servers': kafka_bootstrap},
    #                                     topic='demo-output'))
    # )

if __name__ == '__main__':
  run_pipeline()
    