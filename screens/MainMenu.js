import React, { Component } from 'react';
import {Platform, StyleSheet, Text, View, Button, Alert} from 'react-native';

export default class MainMenu extends Component{
  render(){
    return(
      <View style={styles.container}>

        <View style={styles.viewMargin}/>

        <View style={styles.mainView}>

            <Button onPress = {() => {Alert.alert('Pressed START GAME button');}}
                    style={styles.btn}
                    title='START GAME'
                    />
            <Button onPress = {() => {Alert.alert('Pressed LOAD GAME button');}}
                    style={styles.btn}
                    title='LOAD GAME'
                    />
            <Button onPress = {() => {Alert.alert('Pressed SETTINGS button');}}
                    style={styles.btn}
                    title='SETTINGS'
                    />
            <Button onPress = {() => {Alert.alert('Pressed QUIT button');}}
                    style={styles.btn}
                    title='QUIT'
                    />

        </View>

        <View style={styles.viewMargin}/>

      </View>
    )
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  viewMargin: {
    flex: 1,
    flexDirection: 'column',
  },
  viewMarginRow: {
    flex: 1,
    flexDirection:'row',
  },
  mainViewRow: {
    flex: 4,
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  mainView: {
    flex: 4,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  },
  btn: {
    width: 100,
    height: 35,
  },
});
