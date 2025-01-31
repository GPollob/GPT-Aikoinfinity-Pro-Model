import tensorflow as tf
import tensorflow_quantum as tfq
import cirq

def create_quantum_circuit():
    qubits = cirq.GridQubit.rect(1, 2)
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),
        cirq.CNOT(qubits[0], qubits[1])
    )
    return circuit

class QuantumLayer(tf.keras.layers.Layer):
    def __init__(self):
        super().__init__()
        self.circuit = tfq.convert_to_tensor([create_quantum_circuit()])
        self.readout = tf.keras.layers.Dense(64, activation='relu')

    def call(self, inputs):
        quantum_inputs = tfq.resolve_parameters(
            self.circuit, {}, []
        )
        expectation = tfq.layers.Expectation()(quantum_inputs, operators=tfq.convert_to_tensor([cirq.Z(qubits[0])]))
        return self.readout(expectation)