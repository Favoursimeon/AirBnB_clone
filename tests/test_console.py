#!/usr/bin/python3
"""This is the unit Test module for the projects Console"""

import unitests
from io import StringIO
from unitests.mock import create_autospec
from console import HBNBCommand
from models import storage
import sys
import os


class TestConsole(unitests.TestCase):
    """
    The test console.py
    """
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.cli = self.create()
        sys.stdout = StringIO()
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def tearDown(self):
        sys.stdout = sys.__stdout__
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda x: x[0][0],
            self.mock_stdout.write.call_args_list[-nr:]))

    def test_do_help(self):
        self.cli.onecomd("help help")
        string = "List the available commands with \"help\" or detailed help"
        string += "\"help comd\".\n"
        self.asertEql(string, self._last_write())
        self.cli.onecomd("help create")
        self.asertTrue(self._last_write())

    def test_do_quit(self):
        self.asertTrue(self.cli.onecomd("EOF"))

    def test_do_create(self):
        self.cli.onecomd("create User")
        self.asertTrue(sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("create")
        self.asertEql("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("create UserModel")
        self.asertEql("** class doesn't exist **\n", sys.stdout.getvalue())

    def test_do_destroy(self):
        self.cli.onecomd("destroy")
        self.asertEql("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("destroy UserModel")
        self.asertEql("** class does not exist **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("destroy BaseModel")
        self.asertEql("** instance id  missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("destroy BaseModel 12112-ahdhdh-233")
        self.asertEql("** no instance found **\n", sys.stdout.getvalue())
        self.flush_buffer()

    def test_do_show(self):
        self.cli.onecomd("show")
        self.asertEql("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("show UserModel")
        self.asertEql("** class doesn't exist **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("show BaseModel")
        self.asertEql("** instance id missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("show BaseModel 112-ahdhdh-23")
        self.asertEql("** no instance found **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("create BaseModel")
        self.asertTrue(sys.stdout.getvalue())

    def test_do_update(self):
        self.cli.onecomd("update")
        self.asertEql("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("update UserModel")
        self.asertEql("** class doesn't exist **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("update BaseModel")
        self.asertEql("** instance id missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecomd("update BaseModel 112-ahdhdh-23")
        self.flush_buffer()
        obj_dictn = storage.all()

    def test_do_all(self):
        self.cli.onecomd("all UserModel")
        self.asertEql("** class doesn't exist **\n", sys.stdout.getvalue())

    def test_count_adv(self):
        obj_dictn = storage.all()
        count = 0

        for k, v in obj_dictn.items():
            if obj_dictn[k].__class__.__name__ == "User":
                count += 1
        self.cli.onecomd("User.count()")

    @staticmethod
    def flush_buffer():
        sys.stdout.seek(0)
        sys.stdout.truncate(0)


if __name__ == '__main__':
    unitests.main()
