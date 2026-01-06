from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

def generate_quantum_random_number():
    circuit = QuantumCircuit(3, 3)

    for i in range(3):
        circuit.h(i)

    circuit.measure([0, 1, 2], [0, 1, 2])

    simulator = Aer.get_backend('qasm_simulator')

    result = simulator.run(circuit, shots=1).result()
    
    counts = result.get_counts()
    binary_number = list(counts.keys())[0]
    
    return int(binary_number, 2)

if __name__ == "__main__":
    print("🔮 Генерация квантового числа...")
    print(f"Результат: {generate_quantum_random_number()}")