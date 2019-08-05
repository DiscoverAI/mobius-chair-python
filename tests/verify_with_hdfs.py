# TODO; integration test with batect
from hdfs import InsecureClient

client = InsecureClient('http://localhost:50070', root='/')
import mobius_chair.writer as mw

print(mw.output_path(fs=client, base_path="", name="my_app", version=1))
