import React from "react";
import { Personality } from "@/types/personality";

type Props = {
  item: Personality;
  isChecked: boolean;
  onToggle: (id: number) => void;
};

export const PersonalityItem: React.FC<Props> = ({ item, isChecked, onToggle }) => {
  return (
    <label className="flex items-center space-x-3 p-3 border rounded-lg cursor-pointer hover:bg-gray-50 transition">
      <input
        type="checkbox"
        checked={isChecked}
        onChange={() => onToggle(item.id)}
        className="h-5 w-5 text-blue-600 rounded focus:ring-blue-500"
      />
      <span className="text-gray-700 font-medium">{item.personality}</span>
    </label>
  );
};