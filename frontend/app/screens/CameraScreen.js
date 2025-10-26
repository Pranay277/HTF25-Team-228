import React, { useEffect, useState, useRef } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native';
import { Camera } from 'expo-camera';

const CameraScreen = ({ navigation }) => {
  const [hasPermission, setHasPermission] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const cameraRef = useRef(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const takePicture = async () => {
    if (cameraRef.current) {
      setIsLoading(true);
      await cameraRef.current.takePictureAsync();
      setTimeout(() => {
        setIsLoading(false);
        navigation.goBack();
      }, 2000);
    }
  };

  if (hasPermission === null) return <View />;
  if (hasPermission === false)
    return (
      <View style={styles.permissionContainer}><Text style={{ color: '#fff' }}>No access to camera</Text></View>
    );
  if (isLoading)
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#fff" />
        <Text style={styles.loadingText}>AI is analyzing your item...</Text>
      </View>
    );

  return (
    <View style={styles.container}>
      <Camera
        ref={cameraRef}
        style={StyleSheet.absoluteFillObject}
        type={'back'}
        ratio="16:9"
      />
      <View style={styles.controls}>
        <TouchableOpacity style={styles.captureButton} onPress={takePicture}>
          <Text style={styles.captureText}>📸</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
  permissionContainer: { flex: 1, backgroundColor: '#000', alignItems: 'center', justifyContent: 'center' },
  controls: { position: 'absolute', bottom: 40, width: '100%', alignItems: 'center' },
  captureButton: { width: 80, height: 80, backgroundColor: '#fff', borderRadius: 40, alignItems: 'center', justifyContent: 'center', borderWidth: 4, borderColor: '#ddd' },
  captureText: { fontSize: 28 },
  loadingContainer: { flex: 1, backgroundColor: '#000', alignItems: 'center', justifyContent: 'center' },
  loadingText: { color: '#fff', marginTop: 15, fontSize: 18, fontWeight: '600' }
});

export default CameraScreen;
