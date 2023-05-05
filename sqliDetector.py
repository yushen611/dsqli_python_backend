import libinjection



import re

regex_array = [
            [r"(?i).*\bCREATE\b.*", "DANGER"],
            [r"(?i).*\bDROP\b.*", "DANGER"],
            [r"(?i).*\bALTER\b.*", "DANGER"],
            [r"(?i).*\bUPDATED\b.*", "DANGER"],
            [r"(?i).*\bDELETE\b.*", "DANGER"],
            [r"(?i).*\bGRANT\b.*", "DANGER"],
            [r"(?i).*\bREVOKE\b.*", "DANGER"],
            [r"(?i).*\bSLEEP\b.*", "TIME_BASED"],
            [r"(?i).*\bBENCHMARK\b.*", "TIME_BASED"],
            [r"(?i).*\bPG_SLEEP\b.*", "TIME_BASED"],
            [r"(?i).*\bWAITFOR\b.*", "TIME_BASED"],
            [r"(?i).*\bDELAY\b.*", "TIME_BASED"],
            [r"(?i).*\bUNION\b.*\bSELECT\b.*", "UNION_SELECT"],
            [r"(?i).*\bUNION\b.*=.*", "UNION_SELECT"],
            [r"(?i).*\bOR\b.*=.*", "BOOLEAN"],
            [r"(?i)(AND|and)\s+(\S+)\s*=\s*\2", "BOOLEAN"],
            [r"(?i).*\bDATABASE\b.*", "FUNC_BASED"],
            [r"(?i).*\bCOUNT\b.*", "FUNC_BASED"],
            [r"(?i).*\bSUBSTRING\b.*", "FUNC_BASED"],
            [r"(?i).*\bCAST\b.*", "FUNC_BASED"],
            [r"(?i).*\bCONVERT\b.*", "FUNC_BASED"],
            [r"(?i).*\bEXEC\b.*", "FUNC_BASED"],
            [r"(?i).*\bSP_EXECUTESQL\b.*", "FUNC_BASED"],
            [r"(?i).*\bLOAD_FILE\b.*", "FUNC_BASED"],
            [r"(?i).*\bUPDATEXML\b.*", "FUNC_BASED"],
            [r"(?i).*\bINSERTXML\b.*", "FUNC_BASED"],
            [r"(?si).*--.*", "COMMENT"],
            [r"(?i).*\bUPDATEXML\b.*", "ERROR"],
            [r"(?i).*\bGROUP\b.*", "ERROR"],
            [r"(?i).*\bSELECT\b.*\bFROM\b.*\bWHERE\b.*", "ERROR"]
        ]

def detect_sql_injection_type(sql_injection_string):
    pattern_to_type_map = {}
    for regex_info in regex_array:
        regex = regex_info[0]
        sql_injection_type = regex_info[1]
        pattern = re.compile(regex)
        pattern_to_type_map[pattern] = sql_injection_type

    type = ""
    description = ""
    type_num = 0

    for pattern, pattern_type in pattern_to_type_map.items():
        matcher = pattern.match(sql_injection_string)
        if matcher:
            type += pattern_type + ";"
            description = f"The SQL Injection uses {pattern_type} to exploit the query."
            type_num += 1

    if type_num > 1:
        description = "The SQL Injection uses multiple methods to exploit the query."

    if not type:
        type = "Generic SQL Injection"
        description = "The SQL Injection type could not be determined."

    return {"isSQLi": "1", "query": sql_injection_string, "type": type, "description": description}

def isSQLi(parameter:str):
    libinjection_res = libinjection.is_sql_injection(parameter)
    return libinjection_res['is_sqli']
    

def isSQLiAnalyzer(input:str):
    res = {}
    res["query"] = input
    res["isSQLi"] = "0"
    try:
        if isSQLi(input):
            return detect_sql_injection_type(input)
        return res
    except Exception as e:
        print(e)
        return res
    