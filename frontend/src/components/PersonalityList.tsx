import React from "react";
import { Personality } from "@/types/personality";
import { PersonalityItem } from "./PersonalityItem";

type Props = {
  items: Personality[];
  selectedIds: number[];
  onToggle: (id: number) => void;
};

export const PersonalityList: React.FC<Props> = ({ items, selectedIds, onToggle }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
      {items.map((item) => (
        <PersonalityItem
          key={item.id}
          item={item}
          isChecked={selectedIds.includes(item.id)}
          onToggle={onToggle}
        />
      ))}
    </div>
  );
};