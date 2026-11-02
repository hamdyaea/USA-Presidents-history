# U.S. Presidents — Historical Browser

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

Browse the repository's bundled `presidents.json` using a modern Python 3/Tkinter desktop interface. Unlike the historical EasyGUI application, the new version does not download remote images, overwrite files, or depend on a third-party `wget` module. A CLI listing is also provided.

```sh
python3 presidents.py
python3 presidents.py --list
python3 -m unittest discover -s tests -v
```

**Data disclaimer:** This is a historical snapshot, not an automatically updated or independently fact-checked list of current officeholders. Verify dates and biographical details against authoritative sources before publication.

Original code: [old branch](https://github.com/hamdyaea/USA-Presidents-history/tree/old).
