# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from presidents import DATA, description, load_presidents

class PresidentsTests(unittest.TestCase):
    def test_bundled_dataset(self):
        records = load_presidents(DATA)
        self.assertGreater(len(records), 10)
        self.assertIn("George Washington", description(records[0]))
    def test_invalid_data(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text(json.dumps([{"president": "Missing fields"}]))
            with self.assertRaises(ValueError):
                load_presidents(path)

if __name__ == "__main__":
    unittest.main()
