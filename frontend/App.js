javascript
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import { Ionicons } from '@expo/vector-icons';

import HomeScreen from './app/screens/HomeScreen';
import ResultsScreen from './app/screens/ResultsScreen';
import WardrobeScreen from './app/screens/WardrobeScreen';
import CameraScreen from './app/screens/CameraScreen';

const WardrobeStack = createStackNavigator();
function WardrobeStackScreen() {
  return (
    <WardrobeStack.Navigator screenOptions={{ headerShown: false }}>
      <WardrobeStack.Screen name="Wardrobe" component={WardrobeScreen} />
      <WardrobeStack.Screen name="Camera" component={CameraScreen} />
    </WardrobeStack.Navigator>
  );
}

const PlannerStack = createStackNavigator();
function PlannerStackScreen() {
  return (
    <PlannerStack.Navigator screenOptions={{ headerShown: false }}>
      <PlannerStack.Screen name="Home" component={HomeScreen} />
      <PlannerStack.Screen name="Results" component={ResultsScreen} />
    </PlannerStack.Navigator>
  );
}

const Tab = createBottomTabNavigator();
export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          headerShown: false,
          tabBarIcon: ({ color, size }) => {
            let iconName;
            if (route.name === 'My Closet') iconName = 'shirt-outline';
            else iconName = 'home-outline';
            return <Ionicons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: '#ff4081',
          tabBarInactiveTintColor: 'gray',
        })}
      >
        <Tab.Screen name="Planner" component={PlannerStackScreen} />
        <Tab.Screen name="My Closet" component={WardrobeStackScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

