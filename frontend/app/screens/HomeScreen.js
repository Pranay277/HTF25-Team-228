import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>👗 Outfit Planner</Text>
      <Text style={styles.text}>
        Welcome! Select your occasion, style, and weather to get outfit suggestions.
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center', backgroundColor: '#fff' },
  header: { fontSize: 28, fontWeight: 'bold', marginBottom: 20 },
  text: { fontSize: 16, color: '#555' },
});

export default HomeScreen;

