"use client";

import React from "react";
import { Check, Plus } from "lucide-react";

export interface TagOption {
  id: string;
  label: string;
}

interface TagSelectorProps {
  title: string;
  maxSelect?: number;
  options: TagOption[];
  selectedIds: string[];
  onChange: (selectedIds: string[]) => void;
  // テーマ（配色）の指定
  variant?: "blue" | "green";
}

export const TagSelector: React.FC<TagSelectorProps> = ({
  title,
  maxSelect = 5,
  options,
  selectedIds,
  onChange,
  variant = "blue",
}) => {
  // バリアントごとのスタイル定義
  const variantStyles = {
    blue: {
      bg: "bg-blue-50/60",
      border: "border-blue-100",
      activeTag: "bg-blue-600 text-white hover:bg-blue-700",
      inactiveTag:
        "bg-white text-gray-700 border border-gray-200 hover:bg-gray-50",
      countHighlight: "text-blue-600",
    },
    green: {
      bg: "bg-emerald-50/60",
      border: "border-emerald-100",
      activeTag: "bg-emerald-700 text-white hover:bg-emerald-800",
      inactiveTag:
        "bg-white text-gray-700 border border-gray-200 hover:bg-gray-50",
      countHighlight: "text-emerald-700",
    },
  };

  const style = variantStyles[variant];

  const handleToggle = (id: string) => {
    const isSelected = selectedIds.includes(id);

    if (isSelected) {
      // 選択解除
      onChange(selectedIds.filter((item) => item !== id));
    } else {
      // 最大選択数のチェック
      if (selectedIds.length >= maxSelect) return;
      // 選択追加
      onChange([...selectedIds, id]);
    }
  };

  return (
    <div
      className={`p-6 rounded-2xl border ${style.bg} ${style.border} space-y-4`}
    >
      {/* タイトル領域 */}
      <div className="flex items-center gap-2">
        <h3 className="font-bold text-gray-800 text-base">{title}</h3>
        <span className="text-xs text-gray-500 font-medium">
          （最大{maxSelect}つまで選択可）
        </span>
      </div>

      {/* タグ一覧 */}
      <div className="flex flex-wrap gap-2.5">
        {options.map((option) => {
          const isSelected = selectedIds.includes(option.id);
          const isMaxReached = selectedIds.length >= maxSelect;
          const isDisabled = !isSelected && isMaxReached;

          return (
            <button
              key={option.id}
              type="button"
              onClick={() => handleToggle(option.id)}
              disabled={isDisabled}
              className={`
                flex items-center gap-1.5 px-4 py-2 rounded-full text-sm font-semibold transition-all duration-200 shadow-sm
                ${
                  isSelected
                    ? style.activeTag
                    : `${style.inactiveTag} ${
                        isDisabled
                          ? "opacity-50 cursor-not-allowed"
                          : "cursor-pointer"
                      }`
                }
              `}
            >
              {isSelected ? (
                <Check className="w-4 h-4 stroke-[2.5]" />
              ) : (
                <Plus className="w-4 h-4 stroke-[2.5] text-gray-600" />
              )}
              <span>{option.label}</span>
            </button>
          );
        })}
      </div>

      {/* 選択中のカウント表記 */}
      <div className="text-xs text-gray-500 font-medium">
        選択中 :{" "}
        <span className={`font-bold text-sm ${style.countHighlight}`}>
          {selectedIds.length}
        </span>{" "}
        / {maxSelect}
      </div>
    </div>
  );
};