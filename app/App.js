import React, {Component} from 'react';
import {
  Platform,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  TextInput, 
  Text,
  View} from 'react-native';
import Login from '../components/loginModal';

type Props = {};
export default class App extends Component{
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.header}>
          <Text style = {styles.headerText}>Começo de dois garotos milhonarios</Text>
        </View>
        <Login></Login>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#333',
  },
  header: {
    height: (Platform.OS === 'ios') ? 70 : 50,
    paddingTop: (Platform.OS === 'ios') ? 20: 0,
    backgroundColor: '#FFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerText: {
    fontSize: 16,
    fontWeight: 'bold'
  },
});
