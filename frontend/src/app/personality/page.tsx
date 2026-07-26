"use client";

import React from "react";
import { useRouter } from "next/navigation";
import { usePersonality } from "@/hooks/usePersonality";
import { PersonalityList } from "@/components/PersonalityList";

export default function PersonalityPage() {
  const router = useRouter();
  const { personalities, selectedIds, isLoading, error, handleToggle, savePersonalities } = usePersonality();

  const handleNext = async () => {
    if (selectedIds.length === 0) {
      alert("最低1つ以上の項目を選択してください。");
      return;
    }

    try {
      // 📝 仮のユーザーID (1) を指定して、フック側の保存ロジックを実行
      await savePersonalities();
      
      // 次の特徴・キーワード選択ページへ遷移
      router.push("/features");
    } catch (err) {
      alert("データの保存に失敗しました。もう一度お試しください。");
    }
  };

  if (isLoading) return <div className="p-8 text-center">データを読み込み中...</div>;
  if (error) return <div className="p-8 text-red-500 text-center">エラー: {error}</div>;

  return (
    <main className="max-w-2xl mx-auto p-6">
      <div className="mb-8 text-center">
        <h1 className="text-2xl font-bold text-gray-800">性格・特徴の選択</h1>
        <p className="text-gray-500 mt-2">あなた自身に当てはまるものをすべて選択してください</p>
      </div>

      <PersonalityList
        items={personalities}
        selectedIds={selectedIds}
        onToggle={handleToggle}
      />

      <div className="mt-8 flex justify-end">
        <button
          onClick={handleNext}
          className="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition"
        >
          次へ進む
        </button>
      </div>
    </main>
  );
}