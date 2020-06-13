# Mass Programming Resistance

Source content, configuration, and code for creating [Mass Programming
Resistance](https://mpr.crossjam.net/)

```
python3 -m venv pympr
source pympr/bin/activate
python3 -m pip install --upgrade pip
git clone git@github.com:crossjam/mpr.git
cd mpr
python3 -m pip install -r requirements.txt
git submodule update --init --recursive --remote
make rsync_upload
```

