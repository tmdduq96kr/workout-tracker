import streamlit as st
from datetime import datetime, timedelta
import json
import os

# 운동 루틴 데이터 - OR 옵션 포함
NOVICE_ROUTINE = {
    "Monday": [
        {
            "options": [
                {"name": "Barbell Squats", "sets": 3, "reps": "4-8"},
                {"name": "Hack Squats", "sets": 3, "reps": "6-10"}
            ]
        },
        {
            "options": [
                {"name": "EZ bar curls", "sets": 3, "reps": "6-8"},
                {"name": "DB curls", "sets": 3, "reps": "6-10"}
            ]
        },
        {
            "options": [
                {"name": "Dips", "sets": 3, "reps": "6-8"},
                {"name": "Bench", "sets": 3, "reps": "6-8"}
            ]
        },
        {
            "options": [
                {"name": "DB rows", "sets": 3, "reps": "8-12"},
                {"name": "Cable rows", "sets": 3, "reps": "10-15"}
            ]
        },
        {
            "options": [
                {"name": "Rope triceps extension", "sets": 3, "reps": "10-15"},
                {"name": "Katana extension", "sets": 3, "reps": "10-12"}
            ]
        },
        {
            "options": [
                {"name": "Cable lateral raises", "sets": 3, "reps": "10-15"},
                {"name": "Powell raises", "sets": 3, "reps": "10-12"}
            ]
        },
        {
            "options": [
                {"name": "Sit-ups", "sets": 3, "reps": "10-12"},
                {"name": "Cannonball crunches", "sets": 3, "reps": "8-10"}
            ]
        }
    ],
    "Wednesday": [
        {
            "options": [
                {"name": "Barbell OHP", "sets": 3, "reps": "6-10"},
                {"name": "DB OHP", "sets": 3, "reps": "8-12"}
            ]
        },
        {
            "options": [
                {"name": "Hammer curls", "sets": 3, "reps": "6-10"},
                {"name": "Reverse curls", "sets": 3, "reps": "6-12"}
            ]
        },
        {
            "options": [
                {"name": "Neutral-ups", "sets": 3, "reps": "4-6"},
                {"name": "Neutral grip lat pulldowns", "sets": 3, "reps": "8-12"}
            ]
        },
        {
            "options": [
                {"name": "Leg curls", "sets": 3, "reps": "12-15"},
                {"name": "Hyperextensions", "sets": 3, "reps": "10-12"}
            ]
        },
        {
            "options": [
                {"name": "Split squats", "sets": 3, "reps": "8-12"},
                {"name": "Leg extensions", "sets": 3, "reps": "10-15"}
            ]
        },
        {
            "options": [
                {"name": "DB fly press", "sets": 3, "reps": "10-12"},
                {"name": "Cable flies", "sets": 3, "reps": "12-15"}
            ]
        },
        {
            "options": [
                {"name": "Neck curls", "sets": 3, "reps": "15-20"},
                {"name": "Neck extensions", "sets": 3, "reps": "15-20"}
            ]
        }
    ],
    "Friday": [
        {
            "options": [
                {"name": "Romanian Deadlifts", "sets": 3, "reps": "6-12"},
                {"name": "Barbell Row", "sets": 3, "reps": "8-12"}
            ]
        },
        {
            "options": [
                {"name": "Seated calf raises", "sets": 3, "reps": "15-20"}
            ]
        },
        {
            "options": [
                {"name": "Incline press", "sets": 3, "reps": "6-10"},
                {"name": "Ring push-ups", "sets": 3, "reps": "10-12"}
            ]
        },
        {
            "options": [
                {"name": "DB preacher curls", "sets": 3, "reps": "8-10"},
                {"name": "Bayesian curls", "sets": 3, "reps": "12-15"}
            ]
        },
        {
            "options": [
                {"name": "Leg press", "sets": 3, "reps": "8-12"},
                {"name": "Smith machine squats", "sets": 3, "reps": "8-10"}
            ]
        },
        {
            "options": [
                {"name": "Skull-crushers", "sets": 3, "reps": "8-12"},
                {"name": "French press", "sets": 3, "reps": "8-10"}
            ]
        },
        {
            "options": [
                {"name": "Hanging knee raises", "sets": 3, "reps": "AMRAP"},
                {"name": "Leg raises", "sets": 3, "reps": "AMRAP"}
            ]
        }
    ]
}

# 데이터 저장/불러오기 함수
def load_workout_schedule():
    if os.path.exists('workout_schedule.json'):
        with open('workout_schedule.json', 'r') as f:
            return json.load(f)
    return {}

def save_workout_schedule(schedule):
    with open('workout_schedule.json', 'w') as f:
        json.dump(schedule, f)

def load_workout_progress():
    if os.path.exists('workout_progress.json'):
        with open('workout_progress.json', 'r') as f:
            return json.load(f)
    return {}

def save_workout_progress(progress):
    with open('workout_progress.json', 'w') as f:
        json.dump(progress, f)

def load_exercise_choices():
    if os.path.exists('exercise_choices.json'):
        with open('exercise_choices.json', 'r') as f:
            return json.load(f)
    return {}

def save_exercise_choices(choices):
    with open('exercise_choices.json', 'w') as f:
        json.dump(choices, f)

def load_workout_history():
    if os.path.exists('workout_history.json'):
        with open('workout_history.json', 'r') as f:
            return json.load(f)
    return {}

def save_workout_history(history):
    with open('workout_history.json', 'w') as f:
        json.dump(history, f)

# Streamlit 앱 시작
st.set_page_config(page_title="나의 운동 트래커", page_icon="💪", layout="wide")
st.title("💪 운동 트래커 - Novice")

# 세션 상태 초기화
if 'schedule' not in st.session_state:
    st.session_state.schedule = load_workout_schedule()
if 'progress' not in st.session_state:
    st.session_state.progress = load_workout_progress()
if 'exercise_choices' not in st.session_state:
    st.session_state.exercise_choices = load_exercise_choices()
if 'workout_history' not in st.session_state:
    st.session_state.workout_history = load_workout_history()

# 탭 생성
tab1, tab2, tab3 = st.tabs(["📅 오늘의 운동", "📆 운동 계획", "📊 진행 상황"])

with tab1:
    st.header("오늘의 운동")
    
    # 날짜 선택
    selected_date = st.date_input(
        "날짜 선택",
        value=datetime.now(),
        format="YYYY-MM-DD"
    )
    date_str = selected_date.strftime("%Y-%m-%d")
    
    # 해당 날짜에 할당된 루틴 확인
    if date_str in st.session_state.schedule:
        routine_name = st.session_state.schedule[date_str]
        st.success(f"오늘은 **{routine_name} 루틴** 날입니다!")
        
        # 운동 리스트 표시
        exercise_groups = NOVICE_ROUTINE[routine_name]
        
        # 진행 상황 불러오기
        progress_key = f"{date_str}_{routine_name}"
        choice_key = f"{date_str}_{routine_name}"
        
        if progress_key not in st.session_state.progress:
            st.session_state.progress[progress_key] = {}
        if choice_key not in st.session_state.exercise_choices:
            st.session_state.exercise_choices[choice_key] = {}
        
        completed = 0
        total_exercises = len(exercise_groups)
        
        # 각 운동별 표시
        for idx, exercise_group in enumerate(exercise_groups):
            st.divider()
            
            # OR 선택이 있는 경우
            if len(exercise_group["options"]) > 1:
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    # 운동 선택
                    option_names = [opt["name"] for opt in exercise_group["options"]]
                    default_idx = st.session_state.exercise_choices[choice_key].get(str(idx), 0)
                    
                    selected_idx = st.radio(
                        "선택",
                        range(len(option_names)),
                        format_func=lambda x: option_names[x],
                        key=f"radio_{progress_key}_{idx}",
                        index=default_idx,
                        horizontal=True
                    )
                    
                    st.session_state.exercise_choices[choice_key][str(idx)] = selected_idx
                    selected_exercise = exercise_group["options"][selected_idx]
                
                with col2:
                    # 체크박스와 운동 정보
                    done = st.checkbox(
                        f"{selected_exercise['name']} - {selected_exercise['sets']} sets × {selected_exercise['reps']} reps",
                        key=f"cb_{progress_key}_{idx}",
                        value=st.session_state.progress[progress_key].get(str(idx), False)
                    )
                    
                    # 운동 히스토리 보기
                    with st.expander(f"📊 {selected_exercise['name']} 히스토리"):
                        history = load_workout_history()
                        exercise_history = []
                        
                        # 모든 날짜의 이 운동 기록 찾기
                        for hist_date, routines in history.items():
                            for routine, details in routines.items():
                                if "details" in details:
                                    for ex_idx, ex_data in details["details"].items():
                                        if ex_data["exercise"] == selected_exercise['name']:
                                            exercise_history.append({
                                                "date": hist_date,
                                                "weight": ex_data["weight"],
                                                "reps": ex_data["reps"]
                                            })
                        
                        if exercise_history:
                            # 날짜순 정렬
                            exercise_history.sort(key=lambda x: x["date"], reverse=True)
                            
                            # 최근 5개 기록 표시
                            st.write("**최근 기록:**")
                            for record in exercise_history[:5]:
                                st.write(f"• {record['date']}: {record['weight']}kg × {record['reps']}회")
                            
                            # 최고 기록
                            if any(record["weight"] > 0 for record in exercise_history):
                                max_weight = max(record["weight"] for record in exercise_history if record["weight"] > 0)
                                st.success(f"🏆 최고 무게: {max_weight}kg")
                        else:
                            st.info("아직 기록이 없습니다.")
            else:
                # 선택지가 하나만 있는 경우
                selected_exercise = exercise_group["options"][0]
                done = st.checkbox(
                    f"{selected_exercise['name']} - {selected_exercise['sets']} sets × {selected_exercise['reps']} reps",
                    key=f"cb_{progress_key}_{idx}",
                    value=st.session_state.progress[progress_key].get(str(idx), False)
                )
                
                # 운동 히스토리 보기 (선택지 하나인 경우도 동일하게)
                with st.expander(f"📊 {selected_exercise['name']} 히스토리"):
                    history = load_workout_history()
                    exercise_history = []
                    
                    for hist_date, routines in history.items():
                        for routine, details in routines.items():
                            if "details" in details:
                                for ex_idx, ex_data in details["details"].items():
                                    if ex_data["exercise"] == selected_exercise['name']:
                                        exercise_history.append({
                                            "date": hist_date,
                                            "weight": ex_data["weight"],
                                            "reps": ex_data["reps"]
                                        })
                    
                    if exercise_history:
                        exercise_history.sort(key=lambda x: x["date"], reverse=True)
                        st.write("**최근 기록:**")
                        for record in exercise_history[:5]:
                            st.write(f"• {record['date']}: {record['weight']}kg × {record['reps']}회")
                        
                        if any(record["weight"] > 0 for record in exercise_history):
                            max_weight = max(record["weight"] for record in exercise_history if record["weight"] > 0)
                            st.success(f"🏆 최고 무게: {max_weight}kg")
                    else:
                        st.info("아직 기록이 없습니다.")
            
            if done:
                completed += 1
                st.session_state.progress[progress_key][str(idx)] = True
                
                # 무게와 횟수 입력
                col_weight, col_reps = st.columns(2)
                
                with col_weight:
                    weight_key = f"weight_{progress_key}_{idx}"
                    weight = st.number_input(
                        "무게 (kg)",
                        min_value=0.0,
                        step=2.5,
                        key=weight_key,
                        value=st.session_state.get(weight_key, 0.0)
                    )
                
                with col_reps:
                    reps_key = f"reps_{progress_key}_{idx}"
                    actual_reps = st.text_input(
                        f"실제 횟수 (목표: {selected_exercise['reps']})",
                        key=reps_key,
                        value=st.session_state.get(reps_key, "")
                    )
            else:
                st.session_state.progress[progress_key][str(idx)] = False
        
        # 진행률 표시
        st.divider()
        progress = completed / total_exercises
        st.progress(progress)
        st.write(f"완료: {completed}/{total_exercises} 운동 ({progress*100:.0f}%)")
        
        # 저장 버튼
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 진행 상황 저장", type="primary"):
                # 운동 상세 정보 저장
                workout_details = {
                    "progress": st.session_state.progress[progress_key],
                    "choices": st.session_state.exercise_choices.get(choice_key, {}),
                    "details": {}
                }
                
                # 각 운동의 무게와 횟수 저장
                for idx in range(len(exercise_groups)):
                    if st.session_state.progress[progress_key].get(str(idx), False):
                        weight_key = f"weight_{progress_key}_{idx}"
                        reps_key = f"reps_{progress_key}_{idx}"
                        
                        # 선택된 운동 이름 가져오기
                        exercise_group = exercise_groups[idx]
                        if len(exercise_group["options"]) > 1:
                            selected_idx = st.session_state.exercise_choices[choice_key].get(str(idx), 0)
                            exercise_name = exercise_group["options"][selected_idx]["name"]
                        else:
                            exercise_name = exercise_group["options"][0]["name"]
                        
                        workout_details["details"][str(idx)] = {
                            "exercise": exercise_name,
                            "weight": st.session_state.get(weight_key, 0),
                            "reps": st.session_state.get(reps_key, ""),
                            "date": date_str
                        }
                
                # 기존 히스토리 불러오기
                history = load_workout_history()
                if date_str not in history:
                    history[date_str] = {}
                history[date_str][routine_name] = workout_details
                
                # 저장
                save_workout_history(history)
                save_workout_progress(st.session_state.progress)
                save_exercise_choices(st.session_state.exercise_choices)
                st.success("저장되었습니다!")
        
        # 완료 축하
        if completed == total_exercises:
            st.balloons()
            st.success("🎉 오늘의 운동을 모두 완료했습니다! 수고하셨어요!")
    
    else:
        st.info("이 날짜에는 아직 운동이 계획되지 않았습니다. '운동 계획' 탭에서 루틴을 할당해주세요.")

with tab2:
    st.header("운동 계획 설정")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📌 새 루틴 할당")
        plan_date = st.date_input(
            "날짜 선택",
            value=datetime.now(),
            key="plan_date"
        )
        
        routine = st.selectbox(
            "루틴 선택",
            ["선택하세요", "Monday", "Wednesday", "Friday", "휴식"],
            key="routine_select"
        )
        
        if st.button("루틴 할당", type="primary"):
            if routine != "선택하세요":
                date_str = plan_date.strftime("%Y-%m-%d")
                if routine == "휴식":
                    if date_str in st.session_state.schedule:
                        del st.session_state.schedule[date_str]
                    st.success(f"{plan_date}는 휴식일로 설정되었습니다.")
                else:
                    st.session_state.schedule[date_str] = routine
                    st.success(f"{plan_date}에 {routine} 루틴이 할당되었습니다!")
                save_workout_schedule(st.session_state.schedule)
    
    with col2:
        st.subheader("🗓️ 기존 계획 수정/삭제")
        
        # 예정된 운동 날짜만 표시
        scheduled_dates = sorted([d for d in st.session_state.schedule.keys() 
                                if datetime.strptime(d, "%Y-%m-%d").date() >= datetime.now().date()])
        
        if scheduled_dates:
            selected_scheduled = st.selectbox(
                "수정할 날짜 선택",
                scheduled_dates,
                format_func=lambda x: f"{x} ({st.session_state.schedule[x]} 루틴)"
            )
            
            col_a, col_b = st.columns(2)
            with col_a:
                new_routine = st.selectbox(
                    "새 루틴",
                    ["Monday", "Wednesday", "Friday"],
                    index=["Monday", "Wednesday", "Friday"].index(st.session_state.schedule[selected_scheduled])
                )
            
            with col_b:
                if st.button("✏️ 수정"):
                    st.session_state.schedule[selected_scheduled] = new_routine
                    save_workout_schedule(st.session_state.schedule)
                    st.success("수정되었습니다!")
                    st.rerun()
                
                if st.button("🗑️ 삭제", type="secondary"):
                    del st.session_state.schedule[selected_scheduled]
                    save_workout_schedule(st.session_state.schedule)
                    st.success("삭제되었습니다!")
                    st.rerun()
        else:
            st.info("예정된 운동이 없습니다.")
    
    # 향후 14일 계획 보기
    st.divider()
    st.subheader("📅 향후 2주 운동 계획")
    
    cols = st.columns(7)
    for i in range(14):
        future_date = datetime.now() + timedelta(days=i)
        date_str = future_date.strftime("%Y-%m-%d")
        day_name = future_date.strftime("%a")
        
        with cols[i % 7]:
            if i == 0:
                st.markdown(f"**오늘**")
            else:
                st.caption(f"{future_date.strftime('%m/%d')}")
            
            if date_str in st.session_state.schedule:
                routine = st.session_state.schedule[date_str]
                if routine == "Monday":
                    st.success(f"M")
                elif routine == "Wednesday":
                    st.info(f"W")
                elif routine == "Friday":
                    st.warning(f"F")
            else:
                st.write("🏖️")

with tab3:
    st.header("운동 진행 상황")
    
    # 완료한 운동 세션 표시
    completed_sessions = []
    for key in st.session_state.progress:
        date, routine = key.rsplit('_', 1)
        exercises_done = sum(1 for v in st.session_state.progress[key].values() if v)
        total = len(NOVICE_ROUTINE[routine])
        if exercises_done > 0:
            completed_sessions.append({
                'date': date,
                'routine': routine,
                'completed': exercises_done,
                'total': total,
                'percentage': (exercises_done/total)*100
            })
    
    if completed_sessions:
        # 날짜순 정렬
        completed_sessions.sort(key=lambda x: x['date'], reverse=True)
        
        st.subheader("🏆 운동 기록")
        for session in completed_sessions:
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.write(f"**{session['date']}**")
            with col2:
                st.write(f"{session['routine']} 루틴")
            with col3:
                if session['percentage'] == 100:
                    st.write("✅ 완료!")
                else:
                    st.write(f"{session['percentage']:.0f}%")
        
        # 통계
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("총 운동 일수", f"{len(completed_sessions)}일")
        with col2:
            completed_count = sum(1 for s in completed_sessions if s['percentage'] == 100)
            st.metric("완벽 수행", f"{completed_count}일")
        with col3:
            avg_completion = sum(s['percentage'] for s in completed_sessions) / len(completed_sessions)
            st.metric("평균 완료율", f"{avg_completion:.0f}%")
    else:
        st.info("아직 운동 기록이 없습니다. 오늘부터 시작해보세요!")

# 사이드바에 루틴 정보 표시
with st.sidebar:
    st.header("📋 Novice 루틴 정보")
    for routine_name, exercise_groups in NOVICE_ROUTINE.items():
        with st.expander(f"{routine_name} 루틴"):
            for i, group in enumerate(exercise_groups):
                if len(group["options"]) > 1:
                    opt1 = group["options"][0]
                    opt2 = group["options"][1]
                    st.write(f"{i+1}. **{opt1['name']}** OR **{opt2['name']}**")
                    st.caption(f"   {opt1['sets']}×{opt1['reps']}")
                else:
                    opt = group["options"][0]
                    st.write(f"{i+1}. **{opt['name']}**")
                    st.caption(f"   {opt['sets']}×{opt['reps']}")
                st.write("")
