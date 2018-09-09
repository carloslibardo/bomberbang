import React, {Component} from 'react';
import {
    View,
    Text,
    Modal,
    TextInput,
    TouchableOpacity,
    StyleSheet
} from 'react-native';

export default class LoginModal extends Component {
    render(){
        return (
            <Modal animationType="fade" transparent={true} visible = {true}>
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
                            autoFocus
                            autoCapitalize="none"
                            style={styles.boxInput}
                            placeholder="Digite sua senha"
                        >
                        </TextInput>

                        <View style={styles.buttonContainer}>
                            <TouchableOpacity
                                style={[styles.button, styles.registerButton]}
                                onPress ={() => {}}
                            >
                                <Text style = {styles.buttonText}>Registrar</Text>
                            </TouchableOpacity>

                            <TouchableOpacity
                                style={[styles.button, styles.loginButton]}
                                onPress ={() => {}}
                            >
                                <Text style = {styles.buttonText}>Entrar</Text>
                            </TouchableOpacity>
                        </View>
                    </View>
                </View>
            </Modal>
        )
    }
}

const styles = StyleSheet.create({
   modalContainer: {
       flex: 1,
       backgroundColor: 'rgba(0,0,0, 0.1)',
       justifyContent: 'center' ,
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
   buttonContainer: {
     marginTop: 10,
     height: 40,
     flexDirection: 'row'  
   },
   button: {
       flex: 1,
       alignItems: 'center',
       justifyContent: 'center',
       borderRadius: 3,
   },
   registerButton: {
    backgroundColor: '#E25F5F',
    marginRight: 5,
   },
   loginButton: {
       backgroundColor: '#70BD85',
       marginLeft: 5,
   },
   buttonText:{
       fontWeight:'bold',
       color: "#FFF",
       fontSize: 12,
   }
})