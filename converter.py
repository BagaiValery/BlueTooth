def convert_db_to_distance(signal, basis_length, basis_signal):
    distance = basis_length * (10 ** (basis_signal - signal / 10 * 2))
    return distance
