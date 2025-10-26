import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Image, StyleSheet } from 'react-native';
import { generateOutfit } from '../api/client';

const ResultsScreen = ({ route }) => {
  const [outfitData, setOutfitData] = useState(null);

  useEffect(() => {
    generateOutfit().then(data => setOutfitData(data));
  }, []);

  if (!outfitData) return <Text style={{ margin: 20 }}>Loading...</Text>;

  const renderOutfit = ({ item, index }) => (
    <View style={styles.outfitCard}>
      <View style={styles.imageRow}>
        {item.outfit_items.map((outfitItem, idx) => (
          <Image
            key={outfitItem.image_url + '_' + idx + '_' + index}
            source={{ uri: outfitItem.image_url }}
            style={styles.image}
          />
        ))}
      </View>
      <Text style={styles.explanation}>{item.explanation}</Text>
      <Text style={styles.tip}>Tip: {item.tip}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={outfitData}
        renderItem={renderOutfit}
        keyExtractor={(_, idx) => 'outfitCard_' + idx}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  outfitCard: { marginBottom: 20, padding: 10, backgroundColor: '#f5f5f5', borderRadius: 12 },
  imageRow: { flexDirection: 'row', justifyContent: 'center', marginBottom: 8 },
  image: { width: 120, height: 120, marginHorizontal: 6, borderRadius: 8 },
  explanation: { fontWeight: 'bold', marginBottom: 4 },
  tip: { color: 'gray' },
});

export default ResultsScreen;

