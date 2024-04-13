def generate_latex_table_mediapipe(max_differences):
    latex_table = "\\begin{table}[h]\n"
    latex_table += "\t\\centering\n"
    latex_table += "\t\\begin{tabular}{|c|c|c|}\n"
    latex_table += "\t\t\\hline\n"
    latex_table += "\t\t" + "Měřená proporce" + " & " + "Počet výskytů" + " & " + "Průměrný rozdíl" + " \\\\\n"
    latex_table += "\t\t\\hline\n"
    for key, max_diff in max_differences.items():
        latex_table += "\t\t" + f"{translate_to_czech(key)} & {max_diff.count} & {max_diff.value / max_diff.count:.8f} \\\\\n"
    latex_table += "\t\t\\hline\n"
    latex_table += "\t\\end{tabular}\n"
    latex_table += "\t\\caption{Tabulka výsledků antropometrické analýzy.}\n"
    latex_table += "\t\\label{tab:max-differences}\n"
    latex_table += "\\end{table}"

    return latex_table

def translate_to_czech(key):
    translation_dict = {
        "face_width": "šířka obličeje (zy-zy)",
        "jaw_width": "šířka čelisti (go-go)",
        "lower_face_height": "výška dolní části obličeje (sn-gn)",
        "face_height": "výška obličeje (tr-gn)",
        "morph_face_height": "výška obličeje (n-gn)",
        "upper_face_height": "výška horní části obličeje (n-sto)",
        "lower_third_face_height": "výška dolní třetiny obličeje (sto-gn)",
        "special_face_height_left": "speciální výška obličeje vlevo (en-gn)",
        "special_face_height_right": "speciální výška obličeje vpravo (en-gn)",
        "special_upper_face_height": "speciální výška horní části obličeje (g-sn)",
        "outer_eye_width": "šířka mezi oči vnější (ex-ex)",
        "inner_eye_width": "šířka mezi oči vnitřní (en-en)",
        "left_eye_width": "šířka levého oka (ex-en)",
        "right_eye_width": "šířka pravého oka (ex-en)",
        "nose_width": "šířka nosu (al-al)",
        "nose_height": "výška nosu (n-sn)",
        "mouth_width": "šířka úst (ch-ch)",
        "upper_lip_height": "výška horního rtu (ls-sto)",
        "lower_lip_height": "výška dolního rtu (sto-li)",
    }
    return translation_dict.get(key, key)
