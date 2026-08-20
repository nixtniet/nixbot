# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "4465f93752a9a1e8e31f7c9d8140bebe",
    "brokers": "bf614fd92d3268216c853bbb08a57b03",
    "clients": "9bd824df44ceeeaf73134e38f8177669",
    "command": "2e9fc0aaa8dde0d8caccea26b3feb066",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "36401acdf41a9fde255e2b9d3afbe078",
    "encoder": "7c7f68bbcdc0bd9955c0acf70a9b4d7c",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "loggers": "575e865d11c848de2a53c185a3fb0afc",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "dc4c2e41f7a6cf82584e8119ee6725fa",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "b7edddf1249f1be8b9e568379479948f",
    "package": "2b018b9d8d40aff51bea4e5ddd46c2bd",
    "parsers": "cc9923d5e2e0aab885247a530ac0970c",
    "persist": "49e11f383821f99816f40c5bf2e304d6",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "53ae8d308fceff8dab77fc89f86f7eef",
    "runtime": "0bcce3de89a3f84694c86b7f3054a797",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "timings": "3779158dd2a2f280d403717c7ea75886",
    "utility": "973787cf63dccce61d10b16722c08355"
}


MODULES = {
    "cfg": "e7a4d8f89e5f3442e06af46bf65f5301",
    "eml": "9db4f7401739ac6e5abeb608b81125ef",
    "fie": "0872ed6a02dd678870f502267d9367c6",
    "flt": "1fa811bc0ab9cb5b5b6613ca046f9c3f",
    "fnd": "bb0c19487eee868e39c82ec965b8923d",
    "hlp": "eae0798c461d0e32fb62c1a83830fb89",
    "irc": "7d894f2359776dde8789448b164c6d3d",
    "log": "7d422bf556336c9ece28893b9a0b8356",
    "man": "920599410f7739c9503e0eea9e4e5885",
    "mdl": "a894ae3d8d6ddc6573f3c1b1290dda74",
    "pth": "de5a301a26d1cc548fb53ac4aa5550db",
    "req": "bc1984d2e9de0310dc1b468f25c7ab8c",
    "rss": "9eec6f38ab442e815bcb7a4b6f62a3aa",
    "rst": "524608311cb71e686ab34b65adaf4d17",
    "sil": "942af5ebcf27fc2deb6bbe2d6ca0104c",
    "slg": "e68f11973ddc2e3edeb0de0e16e9fe7a",
    "tdo": "94d259bf3c32c43c3a8667cdf59701ce",
    "thr": "a59544c0c0026efd975cf75e210caeb6",
    "tmr": "74df1496d1c3eec1b65b3641a2456750",
    "udp": "e9a4f41e0f29382335ff6d3d57f980ec",
    "upt": "847a09522abd97a7799a5f5474182064",
    "ver": "e43d64ec467f26dcb0549eaa4d7f5794",
    "web": "fe483635228970a1d51f85f80f0abd26",
    "wsd": "f160d4246e688fba633ae35bd45c7788"
}


NAMES = {
    "atr": "rss",
    "cfg": "cfg",
    "dis": "mdl",
    "dne": "tdo",
    "dpl": "rss",
    "eml": "eml",
    "err": "rss",
    "exp": "rss",
    "fie": "fie",
    "flt": "flt",
    "fnd": "fnd",
    "hlp": "hlp",
    "imp": "rss",
    "log": "log",
    "lou": "sil",
    "man": "man",
    "mbx": "eml",
    "nme": "rss",
    "now": "mdl",
    "pth": "pth",
    "pwd": "irc",
    "rem": "rss",
    "req": "req",
    "res": "rss",
    "rss": "rss",
    "sil": "sil",
    "slg": "slg",
    "syn": "rss",
    "tdo": "tdo",
    "thr": "thr",
    "tmr": "tmr",
    "udp": "udp",
    "upt": "upt",
    "ver": "ver",
    "wsd": "wsd"
}


def __dir__():
    return (
        'CORE',
        'MODULES',
        'NAMES'
    )
