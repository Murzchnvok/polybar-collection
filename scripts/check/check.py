import subprocess

from utils.parser import args

# systemctl is-active nftables.service | tr a-z A-Z
# subprocess.run(["systemctl", "is-active", "nftables.service"])


class Service:
    def __init__(self, service_name):
        self.service_name = service_name

    def status(self):
        return subprocess.run(
            ["systemctl", "is-active", f"{self.service_name}.service"]
        )

    def color(self):
        if self.status == "active":
            return "green"
        return "red"


if __name__ == "__main__":
    if args.service:
        service = Service(args.service[0])
        if args.color:
            print(service.color())
        else:
            service.status()
    else:
        print("You need to pass a service name")
