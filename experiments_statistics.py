from helpers.generate_latex_table import generate_latex_table_mediapipe, create_latex_table_tfi

dash = '-' * 45  # Length of the dashed line

def calculate_average(data):
    return sum(data) / len(data)

def print_analysis_statistics(max_differences):
    print("\n\t\tMediaPipe Summary".upper())
    print(dash)
    print("Max differences:".upper())
    for key, max_diff in max_differences.items():
        print(f"  {key}: {max_diff.count} occurrences, average distance difference: {max_diff.value / max_diff.count}")

    if max_differences:
        # Finding which proportion differs the most
        most_differing_proportion = max(max_differences, key=lambda k: max_differences[k].count)
        print(f"\nThe most differing proportion: {most_differing_proportion}")
        print(f"  Occurrences: {max_differences[most_differing_proportion].count}")
        print(f"  Average distance difference: {max_differences[most_differing_proportion].value / max_differences[most_differing_proportion].count}")
    else:
        print("\nNo differences found.")

    latex_table = generate_latex_table_mediapipe(max_differences)
    # print(latex_table)

def print_tfi_statistics(real_facial_height, real_facial_width, real_tfi, gen_facial_height, gen_facial_width, gen_tfi):
    MHF_real = calculate_average(real_facial_height)
    MFB_real = calculate_average(real_facial_width)
    TFI_real = calculate_average(real_tfi)

    MHF_gen = calculate_average(gen_facial_height)
    MFB_gen = calculate_average(gen_facial_width)
    TFI_gen = calculate_average(gen_tfi)

    MHF_combined = real_facial_height + gen_facial_height
    MHF_avg_combined = calculate_average(MHF_combined)

    MFB_combined = real_facial_width + gen_facial_width
    MFB_avg_combined = calculate_average(MFB_combined)

    TFI_combined = real_tfi + gen_tfi
    TFI_avg_combined = calculate_average(TFI_combined)
    print("\n\t\tTFI Statistics".upper())
    data = [
        ["Parameters", "Real", "Generated", "Combined"],
        ["MFH", MHF_real, MHF_gen, MHF_avg_combined],
        ["MFB", MFB_real, MFB_gen, MFB_avg_combined],
        ["TFI", TFI_real, TFI_gen, TFI_avg_combined]
    ]

    for i in range(len(data)):
        if i == 0:
            print(dash)
            print('{:<10s}{:>10s}{:>12s}{:>12s}'.format(data[i][0], data[i][1], data[i][2], data[i][3]))
            print(dash)
        else:
            print('{:<10s}{:>10.5f}{:>12.5f}{:>12.5f}'.format(data[i][0], data[i][1], data[i][2], data[i][3]))

    print(dash)
    latex_table = create_latex_table_tfi(MHF_real, MHF_gen, MHF_avg_combined, MFB_real, MFB_gen, MFB_avg_combined, TFI_real, TFI_gen, TFI_avg_combined)
    # print(latex_table)
    
def print_verification_statistics_deepface(verification_results, distances):
    success_count = verification_results.count(True)
    failure_count = verification_results.count(False)
    total_pairs = len(verification_results)

    print("\n\t\tDeepface Summary".upper())
    print(dash)

    if total_pairs == 0:
        print("  No pairs to verify.")
        return

    avg_distance = calculate_average(distances)

    sorted_distances = sorted(distances)
    median_index = len(sorted_distances) // 2
    median_distance = sorted_distances[median_index]

    print(f"  Total Pairs: {total_pairs}")
    print(f"  Successful Verifications: {success_count}")
    print(f"  Failed Verifications: {failure_count}")
    print(f"  Average Distance: {avg_distance:.8f}")
    print(f"  Median Distance: {median_distance:.8f}")

    success_rate = (success_count / total_pairs) * 100
    print(f"  Success Rate: {success_rate:.2f}%")