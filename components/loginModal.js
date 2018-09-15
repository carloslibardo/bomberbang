import React, { Component } from 'react';
import {
    View,
    Text,
    Modal,
    TextInput,
    TouchableOpacity,
    StyleSheet,
    Alert
} from 'react-native';

export default class LoginModal extends Component {

    render() {
        return (
            <Modal
                animationType="fade"
                transparent={true}
                visible={this.props.visible}
                onRequestClose={() => {
                    Alert.alert('Modal has been closed');
                }}
            >
                <View style={styles.modalContainer}>
                    <View style={styles.boxContainer}>
                        <Text style={styles.boxTitle}>Faça seu login</Text>
                        <TextInput
                            autoFocus
                            autoCapitalize="none"
                            style={styles.boxInput}
                            placeholder="Digite seu usuário"
                        >
                        </TextInput>
                        <TextInput
                            autoCapitalize="none"
                            style={styles.boxInput}
                            placeholder="Digite sua senha"
                        >
                        </TextInput>
                    </View>
                </View>
            </Modal>
        )
    }
}

const styles = StyleSheet.create({
    modalContainer: {
        flex: 1,
        backgroundColor: 'rgba(0,0,0, 0.7)',
        justifyContent: 'center',
        alignItems: 'center',
    },
    boxContainer: {
        padding: 20,
        backgroundColor: '#FFF',
        borderRadius: 10,
        alignItems: 'center',
        width: 280,
        height: 200
    },
    boxTitle: {
        fontWeight: 'bold',
        fontSize: 16,
    },
    boxInput: {
        alignSelf: 'stretch',
        marginTop: 10,
        paddingVertical: 0,
        paddingHorizontal: 20,
        borderWidth: 1,
        borderColor: '#DDD',
        height: 40,
        borderRadius: 3
    },
})