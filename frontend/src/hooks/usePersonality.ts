import { useState, useEffect } from "react";
import { Personality } from "@/types/personality";
// 💡 既存のapi.tsから共通の通信関数をインポート（実際の関数名に書き換えてください）
import { api } from "@/lib/api"; 

export function usePersonality() {
  const [personalities, setPersonalities] = useState<Personality[]>([]);
  const [selectedIds, setSelectedIds] = useState<number[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // 1. 性格マスタの取得処理
  useEffect(() => {
    async function loadData() {
      try {
        setIsLoading(true);
        // 💡 既存の共通GET関数を利用してエンドポイントを直接叩く
        const data = await api.get<Personality[]>("/personalities");
        setPersonalities(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "予期せぬエラーが発生しました");
      } finally {
        setIsLoading(false);
      }
    }
    loadData();
  }, []);

  // 2. チェックボックスの変更ハンドラー
  const handleToggle = (id: number) => {
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((item) => item !== id) : [...prev, id]
    );
  };

  // 3. データの保存処理（既存の共通POST関数を利用）
  const savePersonalities = async () => {
    // 💡 既存の共通POST関数にパスとペイロードを渡す
    await api.post("/api/user/personalities", {
      personality_ids: selectedIds,
    });
  };

  return {
    personalities,
    selectedIds,
    isLoading,
    error,
    handleToggle,
    savePersonalities,
  };
}