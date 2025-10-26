import React, { useEffect, useState } from 'react';
import { View, FlatList, Image, StyleSheet, TouchableOpacity, Text } from 'react-native';
import { fetchWardrobe } from '../api/client';

const WardrobeScreen = ({ navigation }) => {
  const [wardrobeItems, setWardrobeItems] = useState([]);

  useEffect(() => {
    fetchWardrobe().then(data => setWardrobeItems(data));
  }, []);

  return (
    <View style={styles.container}>
      <FlatList
        data={wardrobeItems}
        numColumns={2}
        renderItem={({ item }) => (
          <Image
            source={{ uri: item.image_url }}
            style={styles.image}
          />
        )}
        keyExtractor={item => item.id + '-' + item.image_url}
        contentContainerStyle={{ padding: 16 }}
      />
      <TouchableOpacity style={styles.fab} onPress={() => navigation.navigate('Camera')}>
        <Text style={styles.fabIcon}>＋</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  image: {
    width: 160,
    height: 160,
    margin: 8,
    borderRadius: 12,
    backgroundColor: '#eee',
  },
  fab: {
    position: 'absolute',
    right: 30,
    bottom: 30,
    width: 60,
    height: 60,
    backgroundColor: '#007aff',
    borderRadius: 30,
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 5,
  },
  fabIcon: { color: '#fff', fontSize: 36, fontWeight: 'bold' },
});

export default WardrobeScreen;
