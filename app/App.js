import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View,
  Image
} from 'react-native';
import Login from '../components/loginModal';
import LoginFooter from '../components/loginFooter';
import { createStore, bindActionCreators } from 'redux';
import { Provider } from 'react-redux';

const initialState = {
  modalVisible: false
}

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case 'ENABLE_MODAL':
      return { modalVisible: true }
  }

  return state;
}

const store = createStore(reducer);

type Props = {};
export default class App extends Component {
  state = {
    modalVisible: false,
  }
  render() {
    return (
      <View >
        <View style={styles.header}>
          <Text style={styles.headerText}>Começo de dois garotos milhonarios</Text>
        </View>
        <Image
          style={{ width: 360, height: 400 }}
          source={require('../components/pp.jpeg')}
        >
        </Image>
        <Provider store={store}>
          <LoginFooter></LoginFooter>
        </Provider>
        <Login visible={this.state.modalVisible}></Login>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  header: {
    height: (Platform.OS === 'ios') ? 70 : 50,
    paddingTop: (Platform.OS === 'ios') ? 20 : 0,
    backgroundColor: '#FFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerText: {
    fontSize: 16,
    fontWeight: 'bold'
  },

});
