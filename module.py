import json


class Module:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.processes_to_track = []

    def get_processes_to_track(self):
        return json.loads(self.get_json())

    def get_json(self):
        self.file = open("modules/" + self.filename)
        return self.file.read()
