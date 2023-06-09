import React from "react";
import { Canvas } from "react-three-fiber";
import { Box } from "@react-three/drei";

function Background() {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <Box position={[-1.2, 0, 0]}>
        <meshStandardMaterial color="purple" />
      </Box>
      <Box position={[1.2, 0, 0]}>
        <meshStandardMaterial color="orange" />
      </Box>
    </Canvas>
  );
}

export default Background;
