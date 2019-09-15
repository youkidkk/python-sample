import json

jsonstr = """
{
    "sample1" : "sample1 text",
    "sample2" : {
        "sample2-1" : "sample2-1 text",
        "sample2-2" : "sample2-2 text",
        "sample2-3" : "sample2-3 text"
    }
}
"""

# JSON文字列 -> 辞書型
jsondict = json.loads(jsonstr)
print(jsondict)

# 辞書型 -> JSON文字列
jsondump = json.dumps(jsondict, indent=4)
print(jsondump)
