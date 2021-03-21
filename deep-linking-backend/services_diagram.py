# pip install diagrams - https://diagrams.mingrammer.com/docs/getting-started/installation
from diagrams import Cluster, Diagram
from diagrams.aws import compute
from diagrams.aws import database
from diagrams.aws import network


with Diagram(filename="bunch_deep_link", show=True):
    before_app = network.Route53("DNS record") >> network.CloudFront("Protection Services")
    load_balancer = network.ELB("Load Balancer")
    load_balancer >> compute.EC2("Web Servers") >> database.RDS("Database, Distributed Locks")
    load_balancer >> compute.EC2("Web Servers") >> database.RDS("Database, Distributed Locks")
    load_balancer >> compute.EC2("Web Servers") >> database.RDS("Database, Distributed Locks")

    before_app >> load_balancer
