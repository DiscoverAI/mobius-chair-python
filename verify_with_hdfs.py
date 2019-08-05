from hdfs import InsecureClient
import os

backend = os.environ.get('BACKEND', 'http://localhost:50070')

client = InsecureClient(backend, root='/')
import mobius_chair.writer as mw

print(mw.output_path(fs=client, base_path="", name="my_app", version=1))
